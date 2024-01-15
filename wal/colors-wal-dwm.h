static const char norm_fg[] = "#d6c6a6";
static const char norm_bg[] = "#0a0c0a";
static const char norm_border[] = "#958a74";

static const char sel_fg[] = "#d6c6a6";
static const char sel_bg[] = "#776438";
static const char sel_border[] = "#d6c6a6";

static const char urg_fg[] = "#d6c6a6";
static const char urg_bg[] = "#6B4F39";
static const char urg_border[] = "#6B4F39";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
