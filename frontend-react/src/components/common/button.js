import styled, { keyframes } from "styled-components";

export const MediumBtn = styled.button`
  width: ${(props) => props.size};
  height: 40px;
  background-color: black;
  color: white;
  border-radius: 5px;
  margin: 5px;
`;

const BoundAnimation = keyframes`{
  0% {
    -webkit-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1)
  }
  30% {
    -webkit-transform: scale3d(1.25, .75, 1);
    transform: scale3d(1.25, .75, 1)
  }
  40% {
    -webkit-transform: scale3d(0.75, 1.25, 1);
    transform: scale3d(0.75, 1.25, 1)
  }
  50% {
    -webkit-transform: scale3d(1.15, .85, 1);
    transform: scale3d(1.15, .85, 1)
  }
  65% {
    -webkit-transform: scale3d(.95, 1.05, 1);
    transform: scale3d(.95, 1.05, 1)
  }
  75% {
    -webkit-transform: scale3d(1.05, .95, 1);
    transform: scale3d(1.05, .95, 1)
  }
  100% {
    -webkit-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1)
  }
}`;
export const LoginButton = styled.button`
  animation-duration: 1s;
  animation-fill-mode: both;
  animation-name: bounce;

  border: none;
  width: ${(props) => props.size};
  height: 40px;
  background-color: black;
  color: white;
  margin: 10px 60px;
  &:active,
  &:focus {
    outline: none;
    animation: ${BoundAnimation} 0.5s 1;
  }
`;
