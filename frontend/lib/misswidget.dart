

import 'package:flutter/material.dart';
import 'package:frontend/fullcounterwidget.dart';

class Misswidget extends StatelessWidget {
	const Misswidget({super.key});

	@override
	  Widget build(BuildContext context) {
		return Row(
		mainAxisAlignment: MainAxisAlignment.center,
		children: [
		Fullcounterwidget(title: "Misses"),
		Padding(padding: EdgeInsets.only(right: 5)),
		Fullcounterwidget(title: "Misses")
		],
		) ;
	 }
}
