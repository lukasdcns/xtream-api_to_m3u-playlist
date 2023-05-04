import axios from 'axios';
import fs from 'fs';

const vodsUrl = "http://smart.cwdn.cx/player_api.php?username=a804691ee2&password=12345678&action=get_vod_streams"

axios.get(vodsUrl)
.then((response) => {

    response.data.forEach((vod) => {
      if (vod.name.includes("fr - ") || vod.name.includes("FR - ")) {
        if (!vod.name.includes("(VOSTFR)") && !vod.name.includes("HDCAM") && !vod.name.includes("VOSTFR")) {
          let vodName = vod.name.replace("FR - ", "").replace(/\s*\(\d+\)/, "").replace("/", " ").replace(" - 4K", "").replace(" 4K", "");
  
          const jellyFinFilePath = `exports/vods/jellyfin/${vodName}.strm`;
          const plexFinFilePath = `exports/vods/plex/${vodName}.fr.srt`;
          fs.writeFileSync(jellyFinFilePath, `http://smart.cwdn.cx/movie/a804691ee2/12345678/${vod.stream_id}.${vod.container_extension}`);
          fs.writeFileSync(plexFinFilePath, `http://smart.cwdn.cx/movie/a804691ee2/12345678/${vod.stream_id}.${vod.container_extension}`);
        }
      }
    });
})
.catch((error) => {
  console.log(error);
});
