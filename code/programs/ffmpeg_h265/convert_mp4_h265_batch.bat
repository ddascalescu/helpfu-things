for %%f in (*.mp4) do (
	ffmpeg -i %%f -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k %%~nf_h265.mp4
	del %%f
)
PAUSE
