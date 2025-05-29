

import 'package:flutter/material.dart';

class Togglebutton extends StatefulWidget {
	const Togglebutton({super.key});

@override
State<Togglebutton> createState() => ToggleButtonState();
}

class ToggleButtonState extends State<Togglebutton> {
	bool _flag = false;
	 @override
  Widget build(BuildContext context) {
      return ElevatedButton(
          onPressed: () => setState(() => _flag = !_flag),
          child: Text(_flag ? '!Defense' : 'Defense', style: TextStyle(color: Colors.black),),
          style: ElevatedButton.styleFrom(
            backgroundColor: _flag ? Colors.red : Colors.green, // This is what you need!
          ),
        );
  }

}
