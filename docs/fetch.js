import { initializeApp } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js";
import {
  getDatabase,
  ref,
  onValue,
} from "https://www.gstatic.com/firebasejs/9.0.0/firebase-database.js";

const firebaseConfig = {
  apiKey: "AIzaSyDZOZ8CgjyvZb8nQB9jQpWjRcb6vaLcu7s",
  authDomain: "typus-csc305.firebaseapp.com",
  databaseURL: "https://typus-csc305-default-rtdb.firebaseio.com",
  projectId: "typus-csc305",
  storageBucket: "typus-csc305.appspot.com",
  messagingSenderId: "333001518286",
  appId: "1:333001518286:web:00a06bc2b3abf25cf3b49f",
  measurementId: "G-6T0Q97ZXCS",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);

// Reference to your leaderboard data
const leaderboardRef = ref(database, "leaderboard");

// Fetch the data
onValue(leaderboardRef, (snapshot) => {
  const data = snapshot.val();
  const leaderboardDiv = document.getElementById("leaderboard");

  // Convert data to an array and sort by score in descending order
  const sortedData = Object.values(data).sort((a, b) => b.score - a.score);

  // Create table headers (if not already created in HTML)
  let content = `
        <table>
          <tr>
            <th>Rank</th>
            <th>Name</th>
            <th>Score</th>
            <th>WPM</th>
          </tr>`;

  // Add each player to the table
  sortedData.forEach((player, index) => {
    content += `
          <tr>
            <td>${index + 1}</td>
            <td>${player.name}</td>
            <td>${player.score}</td>
            <td>${player.wpm}</td>
          </tr>`;
  });

  content += "</table>";
  leaderboardDiv.innerHTML = content;
});
