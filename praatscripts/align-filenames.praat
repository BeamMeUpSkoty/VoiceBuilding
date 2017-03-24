select all 
nocheck Remove
clearinfo

filenames = Read Strings from raw text file... ../resources/raw-text/filenames.txt
utterances = Read from file... ../resources/raw-TextGrids/Group3_beeps.TextGrid
sound = Open long sound file... ../resources/raw-audio/group3.flac
plus utterances
View & Edit

a = 0
select utterances 
ni = Get number of intervals... 1
for i to ni
	label$ = Get label of interval... 1 i
	if label$ == "speech" 
		a += 1
		select filenames 
		prompt$ = Get string... a
		select utterances
		Set interval text... 1 i 'prompt$'
	endif
endfor

