import React from "react";
import styled from "styled-components";

import { MediumBtn } from "../components/common/button";
import { MediumInput, InputLabel } from "../components/common/input";

const LoginWrapper = styled.div`
  width: 400px;
  height: 300px;
  border: 1px solid #dddddd;
  border-radius: 4px;
  align-items: center;
  margin: auto;
  background-color: #fafafa;
`;

export const SignUp = () => {
  return (
    <div>
      <LoginWrapper>
        <InputLabel>아이디</InputLabel>
        <MediumInput />
        <InputLabel>비밀번호</InputLabel>
        <MediumInput />
        <MediumBtn size="200px">회원가입</MediumBtn>
      </LoginWrapper>
    </div>
  );
};
