﻿SetKeyDelay,, 50

$d::

   While ( GetKeyState( "d","P" ) ) {

    Click, 385, 233
	Sleep, 25 ;
	Send, {Tab}
    Sleep, 25 ;
	Click, 385, 233

   }

Return