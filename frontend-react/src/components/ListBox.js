import React from "react";
import styled from "styled-components";
import { MediumText, BoldText } from "../components/common/text";

export const BoxWrapper = styled.div`
  display: block;
  margin: 10px;
  border: 1px solid #dddddd;
`;

const ListTitle = ({ title }) => {
  return (
    <div>
      <BoldText size="12">{title}</BoldText>
    </div>
  );
};

const ListContents = ({ list }) => {
  return (
    <div>
      {list.map((item) => (
        <MediumText size="12">
          {item.name} + {item.reps} + {item.sets}
        </MediumText>
      ))}
    </div>
  );
};

export const ListBox = ({ list }) => {
  return (
    <div>
      <BoxWrapper>
        <ListTitle title={list.title}></ListTitle>
        <ListContents list={list.routine}></ListContents>
      </BoxWrapper>
    </div>
  );
};
