// This function will run when the Predict button is clicked
function showPrediction() {
  // For example, randomly predict success or failure
  const success = Math.random() > 0.3; // 70% chance success

  if (success) {
    alert("Prediction: Fertilization is likely to succeed!");
  } else {
    alert("Prediction: Fertilization might fail. Try again.");
  }
}
