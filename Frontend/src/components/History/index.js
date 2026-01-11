import React, { Component } from "react";
import { getHistory } from "../../services/api";
import "./index.css";

class History extends Component {
  state = {
    history: []
  };

  componentDidMount() {
    getHistory().then((data) => {
      this.setState({ history: data });
    });
  }

  render() {
    return (
      <table className="history-table">
        <thead>
          <tr>
            <th>Title</th>
            <th>URL</th>
          </tr>
        </thead>
        <tbody>
          {this.state.history.map((item) => (
            <tr key={item.id}>
              <td>{item.title}</td>
              <td>{item.url}</td>
            </tr>
          ))}
        </tbody>
      </table>
    );
  }
}

export default History;
