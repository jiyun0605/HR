import axios from 'axios';
import { FETCH_MEMOS, ADD_MEMO, DELETE_MEMO, EDIT_MEMO } from './mutations-types';

const memoAPICore = axios.create({
  baseURL: 'http://localhost:8000/api/memos'
});

export function fetchMemos({ commit }) {
  memoAPICore.get('/').then(({ data }) => commit(FETCH_MEMOS, data));
}

export function addMemo({ commit }, payload) {
  memoAPICore.post('/', payload).then(({ data }) => commit(ADD_MEMO, data));
}

export function deleteMemo({ commit }, id) {
  memoAPICore.delete(`/${id}`).then(() => commit(DELETE_MEMO, id));
}

export function updateMemo({ commit }, payload) {
  const { id, content } = payload;
  memoAPICore.put(`/${id}`, content).then(() => commit(EDIT_MEMO, payload));
}

export default {
  fetchMemos,
  addMemo,
  deleteMemo,
  updateMemo
};
