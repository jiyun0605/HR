import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Login } from "./Login";
import { SignUp } from "./SignUp";
import { Main } from "./Main";
import { MyPage } from "./MyPage";

export const Index = () => {
  return (
    <div>
      <Router>
        <Route exact path="/main" component={Main} />
        <Route path="/login" component={Login} />
        <Route path="/signp" component={SignUp} />
        <Route path="/mypage" component={MyPage} />
      </Router>
    </div>
  );
};
