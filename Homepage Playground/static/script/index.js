function animateValue(obj, start, end, duration) {
  let startTimestamp = null;
  const step = (timestamp) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    obj.innerHTML =
      Math.floor(progress * (end - start) + start);
    if (progress < 1) {
      window.requestAnimationFrame(step);
    }
  };
  window.requestAnimationFrame(step);
}

const commits = document.getElementById("commits");
animateValue(commits, 0, 4270, 2500);

const pr = document.getElementById("pr");
animateValue(pr, 0, 2391, 4000);

const codelines = document.getElementById("codelines");
animateValue(codelines, 0, 786543, 5000);

const countries = document.getElementById("countries");
animateValue(countries, 0, 8, 6000);
