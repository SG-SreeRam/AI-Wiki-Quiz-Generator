import React, { Component } from "react";
import GenerateQuiz from "../GenerateQuiz";
import History from "../History";
import "./index.css";

class Home extends Component {
  state = {
    activeTab: "generate"
  };

  render() {
    const { activeTab } = this.state;

    return (
      <div className="home-container">
        <div className="tabs">
          <button onClick={() => this.setState({ activeTab: "generate" })}>
            Generate Quiz
          </button>
          <button onClick={() => this.setState({ activeTab: "history" })}>
            History
          </button>
        </div>

        {activeTab === "generate" && <GenerateQuiz />}
        {activeTab === "history" && <History />}
      </div>
    );
  }
}

export default Home;
