default: main.py.out
	@echo "Built and deployed"
main.py.out: main.py buildozer.spec
	python2 -m buildozer
	adb shell input keyevent KEYCODE_WAKEUP
	cp main.py main.py.out
	chmod +x main.py.out
%.c.out: %.c
	gcc -g -o $@ $< -lrt -lreadline
clean:
	rm -rf *.out
%.py.out: %.py
	cp $< $@
	chmod +x $@
%.pl.out: %.pl
	cp $< $@
	chmod +x $@
%.sh.out: %.sh
	cp $< $@
	chmod +x $@
%.s.out: %.o
	arm-none-eabi-ld -o $@ $<
%.o: %.s
	arm-none-eabi-as -g -o $<.o
%.m.out: %.m
	cp $< $@
	chmod +x $@
