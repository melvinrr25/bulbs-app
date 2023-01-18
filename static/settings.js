var form = document.querySelector("#settings")
var inputColor = document.querySelector('[name="color"]')
var inputBrightness = document.querySelector('[name="brightness"')
var submitButton = document.querySelector('#settings-submit')

form.addEventListener('submit', async function(e){
  e.preventDefault()
  var color = inputColor.value.replace("#", "")
  var brightness = inputBrightness.value
  var options = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ color, brightness }) 
  }
  submitButton.setAttribute('disabled', 'disabled')
  submitButton.value = 'Updating...'

  const response = await fetch('/settings', options);
  const res = await response.json();
  if (res.result == 'ok'){
  } else {
    alert("Theres was a problem talking to the bulb")
  }
  submitButton.value = 'Save'
  submitButton.removeAttribute('disabled')
})
