import React, { Component } from "react";
import "./index.css";

class Login extends Component {
  state = {
    username: "",
    password: ""
  };

  handleChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleLogin = () => {
    // simple demo login
    if (this.state.username) {
      this.props.onLogin();
    }
  };

  render() {
    return (
      <div className="login-container">
        <h2>Login</h2>

        <input
          type="text"
          name="username"
          placeholder="Username"
          onChange={this.handleChange}
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={this.handleChange}
        />

        <button onClick={this.handleLogin}>Login</button>
      </div>
    );
  }
}

export default Login;
