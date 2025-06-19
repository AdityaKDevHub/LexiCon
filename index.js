const prompt = document.getElementById("prompt");
const summary_input = document.getElementById("summary");
const genBtn = document.getElementById("Gen");

genBtn.addEventListener("click", async () => {
  const text = prompt.value.trim();
  if (!text) return;

  genBtn.disabled = true;
  genBtn.textContent = "Generating...";
  summary_input.value = "";

  try {
    const res = await fetch("/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    const result = await res.json();

    summary_input.value = result.summary || "(no summary)";
  } catch (err) {
    summary_input.placeholder = "Summary isn't available right now. Please try again later...";
    console.error("Error:", err);
  } finally {
    genBtn.disabled = false;
    genBtn.textContent = "Generate";
  }
});
