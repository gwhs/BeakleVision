import 'package:flutter/material.dart';
import 'package:frontend/counterwidget.dart';
import 'package:frontend/titlewidget.dart';

class Fullcounterwidget extends StatelessWidget {
	final title;
	final GlobalKey<CounterState> counterState = GlobalKey<CounterState>();
	Fullcounterwidget({super.key, this.title});
  @override
  Widget build(BuildContext context) {
	return Column(
	children: [
		Tittle(text: title),
		Counter(key: counterState)
	],
	) ;
  }

  int? getcount() {
  return counterState.currentState?.getcount();
  }
}
