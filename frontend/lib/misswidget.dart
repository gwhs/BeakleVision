

import 'package:flutter/material.dart';
import 'package:frontend/fullcounterwidget.dart';

class Misswidget extends StatelessWidget {
	final keys;
	const Misswidget({super.key, this.keys});

	@override
	  Widget build(BuildContext context) {
		return Row(
		mainAxisAlignment: MainAxisAlignment.center,
		children: [
		Fullcounterwidget(title: "Misses", key: keys[0],),
		Padding(padding: EdgeInsets.only(right: 5)),
		Fullcounterwidget(title: "Misses", key: keys[1],)
		],
		) ;
	 }
}
