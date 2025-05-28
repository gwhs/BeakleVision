
import 'package:flutter/material.dart';

class Tittle extends StatelessWidget {
	final text;
	const Tittle({super.key, this.text});

	@override
	  Widget build(BuildContext context) {
	 	return Text(
		text,
		textScaler: TextScaler.linear(1.25),
		style: TextStyle(color: Colors.black),
		);
	  }
}
