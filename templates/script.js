// Requiring fs module in which
// writeFile function is defined.
// import {fs} from 'fs'

// Data which will write in a file.
function createGrid() {

  const gridSize = parseInt(document.getElementById('grid-size').value);
  const gridContainer = document.getElementById('grid-container');
  gridContainer.innerHTML = '';
  const buttonSize = Math.min(window.innerWidth, window.innerHeight) / gridSize / 1.1;
  for (let i = 0; i < gridSize; i++) {
    for (let j = 0; j < gridSize; j++) {
      const button = document.createElement('button');
      button.textContent = '';
      button.style.height = buttonSize + "px";
      button.style.width = buttonSize + "px";
      button.addEventListener('click', function() {
        const position = { x: i, y: j };
        console.log(window.location.href)
    });
      gridContainer.appendChild(button);
    }
    const lineBreak = document.createElement('br');
    gridContainer.appendChild(lineBreak);
  }
}
