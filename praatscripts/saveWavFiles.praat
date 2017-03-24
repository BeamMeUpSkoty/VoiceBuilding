# Save selected sounds as seperate wave files

tg = Read from file... ../resources/raw-TexGrids/combined_clean.TextGrid
snd = Open long sound file... ../resources/raw-audio/group3_16k.flac
plus tg
View & Edit

select tg
ni =  Get number of intervals... 1
for i to ni
	label$ = Get label of interval... 1 i
	if label$ != "" 
		intervalStart = Get starting point... 1 i 
		intervalEnd = Get end point... 1 i 
		select snd
		part = Extract part... intervalStart intervalEnd yes
		Write to WAV file... ../resources/wav/'label$'.wav
	endif
	select tg
endfor

echo Done
