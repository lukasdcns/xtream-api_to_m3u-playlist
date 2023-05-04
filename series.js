import axios from 'axios';
import fs from 'fs';


axios.get("http://smart.cwdn.cx/player_api.php?username=a804691ee2&password=12345678&action=get_series")
.then((response) => {
    let series = [];
    response.data.forEach((serie) => {
        if (serie.name.includes("fr - ") || serie.name.includes("FR - ")) {
            let serieName = serie.name.replace("FR - ", "").replace(/\s*\(\d+\)/, "").replace("/", " ").replace(" - 4K", "").replace(" 4K", "");
            let serieInfoUrl = "http://smart.cwdn.cx/player_api.php?username=a804691ee2&password=12345678&action=get_series_info&series_id=" + serie.series_id

            series.push({"name": serieName, "series_id": serie.series_id, "serie_info_url": serieInfoUrl});
        }
    });

    const seriesJsonPath = `exports/series/series.json`;
    fs.writeFileSync(seriesJsonPath, JSON.stringify(series));
})
.finally(() => {
    addEventListener("message", (event) => {
})
.catch((error) => {
    console.log(error);
});