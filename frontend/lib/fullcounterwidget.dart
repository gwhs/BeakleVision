

import 'package:flutter/material.dart';
import 'package:frontend/counterwidget.dart';

class Fullcounterwidget extends StatelessWidget {
	final title;
	final GlobalKey<CounterState> counterState = GlobalKey<CounterState>();
	Fullcounterwidget({super.key, this.title});
  @override
  Widget build(BuildContext context) {
	return Column(
	children: [
		Text(title),
		Counter(key: counterState)
	],
	) ;
  }

  int? getcount() {
  return counterState.currentState?.getcount();
  }
}
