import React from "react";
import "./index.css";

const QuizCard = ({ data }) => {
  return (
    <div className="quiz-card">
      <h3>{data.question}</h3>
      <ul>
        {data.options.map((opt, idx) => (
          <li key={idx}>{opt}</li>
        ))}
      </ul>
      <p><b>Answer:</b> {data.answer}</p>
      <p><b>Difficulty:</b> {data.difficulty}</p>
      <p><b>Explanation:</b> {data.explanation}</p>
    </div>
  );
};

export default QuizCard;
