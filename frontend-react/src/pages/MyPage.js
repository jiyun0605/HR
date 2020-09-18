import React from "react";
import styled from "styled-components";

import { LoginButton } from "../components/common/button";
import { MediumInput, InputLabel } from "../components/common/input";

const LoginWrapper = styled.div`
  width: 400px;
  height: 300px;
  border-radius: 4px;
  align-items: center;
  margin: auto;
  margin-top: 50px;
  background-color: #00000;
  display: flex;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 0px 3px 0px,
    rgba(40, 40, 40, 0.3) 0px 5px 5px 0px;
`;
const LoginBox = styled.div`
  margin: auto;
`;
export const MyPage = () => {
  return (
    <div>
      <LoginWrapper>
        <LoginBox>
          <InputLabel>아이디</InputLabel>
          <MediumInput />
          <InputLabel>비밀번호</InputLabel>
          <MediumInput />
          <LoginButton size="200px">회원가입</LoginButton>
        </LoginBox>
      </LoginWrapper>
    </div>
  );
};
