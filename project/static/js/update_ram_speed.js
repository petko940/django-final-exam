function updateSpeedChoices() {
            const memoryType = document.getElementById('id_memory_type');
            const speedField = document.getElementById('id_speed');
            const ddrValue = memoryType.value;

            const speedChoices = {
                'DDR1': [
                    ['200', '200 MHz'],
                    ['266', '266 MHz'],
                    ['333', '333 MHz'],
                    ['400', '400 MHz']
                ],
                'DDR2': [
                    ['400', '400 MHz'],
                    ['533', '533 MHz'],
                    ['667', '667 MHz'],
                    ['800', '800 MHz'],
                    ['1000', '1000 MHz']
                ],
                'DDR3': [
                    ['800', '800 MHz'],
                    ['1066', '1066 MHz'],
                    ['1333', '1333 MHz'],
                    ['1600', '1600 MHz'],
                    ['1866', '1866 MHz']
                ],
                'DDR4': [
                    ['2133', '2133 MHz'],
                    ['2400', '2400 MHz'],
                    ['2666', '2666 MHz'],
                    ['2933', '2933 MHz'],
                    ['3200', '3200 MHz'],
                ],
                'DDR5': [
                    ['3200', '3200 MHz'],
                    ['3600', '3600 MHz'],
                    ['4000', '4000 MHz'],
                    ['4400', '4400 MHz'],
                    ['4800', '4800 MHz'],
                    ['5200', '5200 MHz'],
                    ['5600', '5600 MHz']
                ]
            };

            const choices = speedChoices[ddrValue] || [];
            speedField.innerHTML = '';

            choices.forEach(function (choice) {
                const option = document.createElement('option');
                option.value = choice[0];
                option.text = choice[1];
                speedField.add(option);
            });
        }

        updateSpeedChoices();