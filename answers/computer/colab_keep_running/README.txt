CRTL + SHIFT + I > Console

Paste this:

function ClickConnect() {
	console.log('Working')
	document
		.querySelector('#top-toolbar > colab-connect-button')
		.shadowRoot.querySelector('#connect')
		.click()
}
setInterval(ClickConnect, 300000)