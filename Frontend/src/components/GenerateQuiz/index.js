import React, { Component } from "react";
import QuizCard from "../QuizCard";
import { generateQuiz } from "../../services/api";
import "./index.css";

class GenerateQuiz extends Component {
  state = {
    url: "",
    quizData: null,
    loading: false
  };

  handleGenerate = async () => {
    this.setState({ loading: true });

    try {
      const data = await generateQuiz(this.state.url);

      if (data.error) {
        alert(data.error);
        this.setState({ loading: false });
        return;
      }

      this.setState({ quizData: data, loading: false });

    } catch (err) {
      alert("Failed to connect to server");
      this.setState({ loading: false });
    }
  };

  render() {
    const { quizData, loading } = this.state;

    return (
      <div className="generate-container">
        <input
          placeholder="Wikipedia URL"
          onChange={(e) => this.setState({ url: e.target.value })}
        />

        <button onClick={this.handleGenerate}>
          {loading ? "Generating..." : "Generate Quiz"}
        </button>

        {quizData && quizData.quiz && quizData.quiz.map((q, index) => (
          <QuizCard key={index} data={q} />
        ))}
      </div>
    );
  }
}

export default GenerateQuiz;
