import React, { Component } from "react";
import Login from "./components/Login";
import Home from "./components/Home";

class App extends Component {
  state = { loggedIn: false };

  render() {
    return this.state.loggedIn ? (
      <Home />
    ) : (
      <Login onLogin={() => this.setState({ loggedIn: true })} />
    );
  }
}

export default App;
