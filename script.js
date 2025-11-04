// script.js
document.getElementById("team-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const homeTeam = document.getElementById("home-team").value;
    const awayTeam = document.getElementById("away-team").value;

    // Send data to the server
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ homeTeam, awayTeam })
        });

        if (!response.ok) {
            throw new Error("Network response was not ok " + response.statusText);
        }

        const predictions = await response.json();

        // Update predictions output
        const output = document.getElementById("predictions-output");
        output.innerHTML = `
            <p><strong>Match:</strong> ${homeTeam} vs ${awayTeam}</p>
            <p><strong>Hollywoodbets Prediction:</strong> Home Win Odds: ${predictions.hollywoodbets.home_win}, Draw Odds: ${predictions.hollywoodbets.draw}, Away Win Odds: ${predictions.hollywoodbets.away_win}</p>
            <p><strong>Betway Prediction:</strong> Home Win Odds: ${predictions.betway.home_win}, Draw Odds: ${predictions.betway.draw}, Away Win Odds: ${predictions.betway.away_win}</p>
            <p><strong>AI Prediction:</strong> ${predictions.aiPrediction}</p>
            <p><strong>Average Odds:</strong> Home Win: ${predictions.avgOdds.home_win}, Draw: ${predictions.avgOdds.draw}, Away Win: ${predictions.avgOdds.away_win}</p>
        `;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById("predictions-output").innerHTML = `<p>Error: ${error.message}</p>`;
    }
});
