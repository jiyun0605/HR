import React from "react";
import styled from "styled-components";
import { ListBox } from "../components/ListBox";

export const InfoWrapper = styled.div`
  display: flex;
  margin: 10px;
`;

export const Info = ({ data }) => {
  const newData = data.list;
  return (
    <div>
      <InfoWrapper>
        {newData.map((item) => (
          <div>
            <ListBox list={item}></ListBox>
          </div>
        ))}
      </InfoWrapper>
    </div>
  );
};
