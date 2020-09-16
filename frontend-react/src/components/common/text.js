import styled from "styled-components";

export const TextWrapper = styled.div`
  width: 300px;
`;

export const MediumText = styled.span`
  font-family: Noto Sans CJK KR;
  font-style: normal;
  font-weight: normal;
  display: flex;
  align-items: center;
  margin: 5px;
  font-size: ${(props) => props.size};
`;

export const BoldText = styled.span`
  font-family: Noto Sans CJK KR;
  font-style: normal;
  font-weight: bold;
  display: flex;
  align-items: center;
  margin: 5px;
  font-size: ${(props) => props.size};
`;
