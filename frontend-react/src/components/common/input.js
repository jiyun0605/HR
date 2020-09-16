import styled from "styled-components";

export const LargeInput = styled.input`
  width: 340px;
  height: 50px;
  box-sizing: border-box;
  padding: 0 10px 0 10px;
  margin: 0;
  font-family: "Noto Sans KR", sans-serif;
  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 24px;
  display: flex;
  align-items: center;
  border-style: solid;
  border-width: 1px;
  border-radius: 4px;
  letter-spacing: -0.0002em;
  color: #000;
`;

export const MediumInput = styled(LargeInput)`
  width: ${(props) => (props.width ? props.width : "320px")};
`;

export const SmallInput = styled(LargeInput)`
  width: 220px;
  ::placeholder {
    text-align: ${(props) =>
      props.placeholderTextAlign ? props.placeholderTextAlign : "left"};
  }
`;

export const InputWrapper = styled.div`
  display: flex;
  flex-flow: column;
  margin-bottom: 10px;
`;

export const InputLabel = styled.label`
  font-size: 14px;
  margin-bottom: 10px;
  font-family: "Noto Sans KR", sans-serif;
`;
