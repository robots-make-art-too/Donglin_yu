var styleId = '__htmlGray'

function getStyleEl() {
  return document.querySelector(`#${styleId}`)
}

function appendGrayStyle() {
  if (getStyleEl()) return

  const style = document.createElement('style')
  style.innerHTML = `
    html {
      filter: blur(10px);
      -webkit-filter: blur(10px);
    }
  `
  style.setAttribute('id', styleId)
  document.head.appendChild(style)
}

function deleteGrayStyle() {
  const style = getStyleEl()
  if (!style) return

  style.parentNode.removeChild(style)
}

chrome.runtime.onMessage.addListener((data, sender, callback) => {
  if (data.msg === 'on') {
    appendGrayStyle()
  } else if (data.msg === 'off') {
    deleteGrayStyle()
  }
})