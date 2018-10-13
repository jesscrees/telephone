# telephone
This is a version of the old whisper game telephone that uses your actual
telephone that is a project for Hackference 2018. 

Flask through ngrok 
`./ngrok http <flask's port>`

Viting /calls will calls the test number and is supposed to redirect to the
answer endpoint to trigger the text to speech, but that's not working yet.

Then we need to set up recording of the person's response, use some sort of
speech to text to parse the audio file in to text. Then call another person and
read the text to them and record their response and so on and so forth.

godspeed

