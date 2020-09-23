import React from "react";
import styled from "styled-components";

import { LoginButton } from "../components/common/button";
import {
  MediumInput,
  InputLabel,
  LoginInput,
} from "../components/common/input";
import { LoginWrapper } from "../components/common/wrapper";

const LoginBox = styled.div`
  margin: auto;
`;
export const SignUp = () => {
  return (
    <div>
      <LoginWrapper>
        <LoginBox>
          <InputLabel>아이디</InputLabel>
          <LoginInput />
          <InputLabel>비밀번호</InputLabel>
          <LoginInput />
          <LoginButton size="200px">회원가입</LoginButton>
        </LoginBox>
      </LoginWrapper>
    </div>
  );
};
