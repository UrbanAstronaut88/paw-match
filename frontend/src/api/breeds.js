import { http } from "./http";

export async function listBreeds(params) {
  const { data } = await http.get("/breeds/", { params });
  return data;
}

export async function getBreed(id) {
  const { data } = await http.get(`/breeds/${id}/`);
  return data;
}

export async function matchBreeds(payload) {
  const { data } = await http.post("/match/", payload);
  return data;
}

export async function compareBreeds(firstId, secondId) {
  const { data } = await http.get(`/breeds/compare/?first=${firstId}&second=${secondId}`);
  return data;
}

export async function addFavorite(breedId) {
  const { data } = await http.post(`/breeds/${breedId}/favorite/`);
  return data;
}

export async function removeFavorite(breedId) {
  const { data } = await http.delete(`/breeds/${breedId}/unfavorite/`);
  return data;
}

export async function listFavorites() {
  const { data } = await http.get("/favorites/");
  return data;
}

export async function listQuizResults(params) {
  const { data } = await http.get("/quiz-results/", { params });
  return data;
}

export async function createQuizResult(payload) {
  const { data } = await http.post("/quiz-results/", payload);
  return data;
}
