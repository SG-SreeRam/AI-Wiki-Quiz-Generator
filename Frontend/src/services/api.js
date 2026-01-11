const BASE_URL = "http://localhost:5000/api";

export const generateQuiz = async (url) => {
  const res = await fetch(`${BASE_URL}/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url })
  });
  return res.json();
};

export const getHistory = async () => {
  const res = await fetch(`${BASE_URL}/history`);
  return res.json();
};
