

import 'package:flutter/material.dart';

class Counter extends StatefulWidget {
	const Counter({super.key});

	@override
	  State<Counter> createState() => CounterState();
}

class CounterState extends State<Counter> {
int counter = 0;
@override
  Widget build(BuildContext context) {
  
	return Row(
	mainAxisAlignment: MainAxisAlignment.center,
	children: [
	TextButton(onPressed: (){
	if (counter-- == 0) {
		  counter = counter;}
	else {
	setState(() {
		  counter--;
		});}
	}, child: Text("-")),
	Text("$counter"),
	TextButton(onPressed: (){
	setState(() {
		  counter++;
		});
	}, child: Text("+"))
	],
	);
  }

  int getcount() {
  return counter;
  }
}
