import React from "react";
import styled from "styled-components";
import respone from "../dummies/data.json";

import { Info } from "../components/info";

const ListWrapper = styled.div`
  border: 1px solid #dddddd;
  box-sizing: border-box;
  border-radius: 4px;
  width: 500px;
  height: 100%;
  margin: 10px;
`;

export const Main = () => {
  const list = respone.data;
  return (
    <div>
      <ListWrapper>
        {list.map((item) => (
          <Info data={item}></Info>
        ))}
      </ListWrapper>
    </div>
  );
};
