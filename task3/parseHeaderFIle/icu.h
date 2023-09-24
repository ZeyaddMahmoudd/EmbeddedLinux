/*
 * icu.h
 *
 *  Created on: Jul 20, 2023
 *      Author: zeyad
 */

#ifndef ICU_H_
#define ICU_H_

typedef enum
{NO_CLOCK, CLOCK, CLOCK_8, CLOCK_64, CLOCK_256, CLOCK_1024, RISING_EXT_T1, FALLING_EXT_T1 } ICU_ClockType;

typedef enum
{FALLING, RISING} ICU_EdgeType;

typedef struct
{  ICU_ClockType clock;
   ICU_EdgeType edge;
}ICU_ConfigType;

#endif /* ICU_H_ */

void ICU_init();

void ICU_setCallBack(void(*a_ptr)(void));

void ICU_setEdgeDetectionType(const ICU_EdgeType edge);

uint16 ICU_getInputCaptureValue(void);

void ICU_clearTimerValue(void);

void ICU_deInit(void);
