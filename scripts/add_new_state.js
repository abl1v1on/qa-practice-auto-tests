const selectElement = document.querySelector('#id_select_state');

const newState = document.createElement('option');
newState.setAttribute('value', 'new-state');
newState.textContent = 'New state';

selectElement.appendChild(newState);
