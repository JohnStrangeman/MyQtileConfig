const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#0a0c0a", /* black   */
  [1] = "#6B4F39", /* red     */
  [2] = "#776438", /* green   */
  [3] = "#5E5647", /* yellow  */
  [4] = "#8E6039", /* blue    */
  [5] = "#976D49", /* magenta */
  [6] = "#779470", /* cyan    */
  [7] = "#d6c6a6", /* white   */

  /* 8 bright colors */
  [8]  = "#958a74",  /* black   */
  [9]  = "#6B4F39",  /* red     */
  [10] = "#776438", /* green   */
  [11] = "#5E5647", /* yellow  */
  [12] = "#8E6039", /* blue    */
  [13] = "#976D49", /* magenta */
  [14] = "#779470", /* cyan    */
  [15] = "#d6c6a6", /* white   */

  /* special colors */
  [256] = "#0a0c0a", /* background */
  [257] = "#d6c6a6", /* foreground */
  [258] = "#d6c6a6",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
