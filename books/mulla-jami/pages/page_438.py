# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 438 (printed ٤٣٧)."""

PAGE_NUMBER = 438
PRINTED_PAGE = "٤٣٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… فتقول: «حضرت القاضي امرأة، وحضر القاضي امرأة،» at the foot of PDF p. 437 (mid-quotation).
    {"type": "matn",
     "ar": "وطلعت اليوم الشمس، وطلع اليوم الشمس»،",
     "en": "…“ṭalaʿat al-yawma al-shamsu” and “ṭalaʿa al-yawma al-shamsu” (the sun rose today);"},
    {"type": "matn",
     "ar": "إلا إذا كان المؤنث الحقيقي منقولا عما يغلب في أسماء الذكور كـ«زيد» إذا سميت به امرأة، فإنه مع الفصل يجب إثباتها، نحو: «جاءت اليوم زيد» لرفع الالتباس.",
     "en": "except when the real feminine is transferred from a name that predominates among male names, like “Zayd” when a woman is named by it; for then, even with separation, it [the tāʾ] must be retained, as in “jāʾat al-yawma Zaydu” (Zayd [a woman] came today), to remove ambiguity."},
    {"type": "matn",
     "ar": "(وحكم ظاهر الجمع) لا ضميره، فإن إلحاق التاء أو ضمير الجمع فيه واجب نحو: «الرجال جاءت أو جاؤوا»",
     "en": "(And the rule of the overt plural), not its pronoun, for with that, adding the tāʾ or the plural pronoun is necessary, as in “al-rijālu jāʾat” or “jāʾū” (the men came),"},
    {"type": "matn",
     "ar": "(غير) جمع (المذكر السالم)؛ لأنه لو كان جمع المذكر السالم لم يجز تأنيثه، فلا يقال: «جاءت الزيدون، ولا الزيدون جاءت»",
     "en": "(other than) the (sound masculine) plural; because if it were a sound masculine plural, making it feminine would not be allowed: one does not say “jāʾat al-Zaydūna”, nor “al-Zaydūna jāʾat”,"},
    {"type": "matn",
     "ar": "(مطلقا) أي: سواء كان واحده مؤنثا[[١]] نحو: «إذا جاءك المؤمنات» أو مذكرا نحو: «جاءت الرجال»",
     "en": "(absolutely), that is, whether its singular is feminine, as in “idhā jāʾaka al-muʾminātu” (when the believing women come to you), or masculine, as in “jāʾat al-rijālu” (the men came),"},
    {"type": "matn",
     "ar": "(حكم ظاهر غير) المؤنث (الحقيقي) فأنت بالخيار، إن شئت ألحقت التاء به، وإن شئت تركتها، نحو: «جاءت الرجال وجاء الرجال».",
     "en": "(is the rule of the overt non-real) feminine: you have the choice; if you wish you add the tāʾ to it, and if you wish you omit it, as in “jāʾat al-rijālu” and “jāʾa al-rijālu”."},
    {"type": "matn",
     "ar": "(وضمير) جمع الذكور (العاقلين) من جمع التكسير[[٢]] (غير) الجمع (المذكر السالم) فإنهم إذا جمعوا سالما، فإن ضميرهم الواو لا غير،",
     "en": "(And the pronoun of) the plural of (rational) males, among broken plurals, (other than the sound masculine) plural (for when they are given a sound plural, their pronoun is the wāw and nothing else:"},
    {"type": "matn",
     "ar": "يقال: «الزيدون جاؤوا» ولا يقال: «جاءت»",
     "en": "one says “al-Zaydūna jāʾū” and does not say “jāʾat”),"},
    {"type": "matn",
     "ar": "(فعلت) أي: ضمير «فعلت»، وهو المستكن فيه المقرون بالتاء الساكنة[[٣]] للتأنيث بتأويل الجماعة نحو: «الرجال جاءت»",
     "en": "(is faʿalat), that is, the pronoun of “faʿalat”, namely the one latent in it, joined to the quiescent tāʾ of the feminine, by construing [them] as a group (jamāʿa), as in “al-rijālu jāʾat”,"},
    {"type": "matn",
     "ar": "(وفعلوا) أي: ضمير «فعلوا» يعني: الواو لكونها موضوعة لهذا النوع من الجمع",
     "en": "(and faʿalū), that is, the pronoun of “faʿalū”, meaning the wāw, since it is coined for this kind of plural."},
    {"type": "matn",
     "ar": "(والنساء والأيام) أي: ضمير النساء وما يماثلها في كونه جمع المؤنث وإن لم يكن من العقلاء، كـ«العيون»،",
     "en": "(And of al-nisāʾ (women) and al-ayyām (days)), that is, the pronoun of “al-nisāʾ” and what resembles it in being a feminine plural, even if not of rational beings, like “al-ʿuyūn” (eyes),"},
    {"type": "matn",
     "ar": "وضمير الأيام وما يماثلها في كونه جمع المذكر[[٤]] غير السالم[[٥]] (فعلت وفعلن) أي: ضمير «فعلت»",
     "en": "and the pronoun of “al-ayyām” and what resembles it in being a masculine plural that is not sound, (is faʿalat and faʿalna), that is, the pronoun of “faʿalat”…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "حقيقي التأنيث كنسوة أو مجازيه كدور أو مذكرا حقيقي التذكير كرجال أو مجازيه كأيام،",
     "en": "Really feminine, like “niswa” (women), or figuratively so, like “dūr” (houses); or masculine, really masculine, like “rijāl” (men), or figuratively so, like “ayyām” (days);"},
    {"type": "pair",
     "ar": "وسواء كان الجمع التكسير كما في الأمثلة المذكورة أو جمع المؤنث السالم كالزينبات والطلحات والجبلات والغرفات،",
     "en": "and whether the plural is broken, as in the examples given, or a sound feminine plural, like “al-Zaynabāt”, “al-Ṭalḥāt”, “al-jabalāt” and “al-ghurufāt”."},
    {"type": "pair",
     "ar": "فهذه صور ثمانية يجوز فيها التاء وتركها.",
     "en": "These are eight cases in which the tāʾ and its omission are both allowed."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الصواب تأخيره عن قوله: غير الجمع المذكر إلى آخره؛ لأنه بيان ما بقي بعد التخصيص، وأن يزاد جمع المؤنث السالم كالطلحات.",
     "en": "The correct thing is to place it after his words “other than the masculine plural…” to the end, because it states what remains after the specification; and to add the sound feminine plural, like “al-Ṭalḥāt”."},
    {"type": "pair",
     "ar": "في الرضي: وضمير العاقلين لا بالواو والنون.",
     "en": "In al-Raḍī: “and the pronoun of rational beings [pluralized] not with wāw and nūn.”"},
    {"type": "pair",
     "ar": "أما الواو نحو: الرجال والطلحات ضربوا نظرا إلى الفعل.",
     "en": "As for the wāw, as in “al-rijālu wa-l-Ṭalḥātu ḍarabū”, it is with regard to the verb."},
    {"type": "pair",
     "ar": "وأما ضمير المؤنث الغائب نحو: الرجال والطلحات فعلت نظرا إلى طريان معنى الجماعة على اللفظ.",
     "en": "As for the pronoun of the absent feminine, as in “al-rijālu wa-l-Ṭalḥātu faʿalat”, it is with regard to the meaning of “group” supervening upon the word."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لكونها علامة عليه. والمقصود أن التاء وإن لم يكن ضميرا فهي دالة عليه، فلذا قامت مقامه.",
     "en": "Because it is a sign of it. What is meant is that the tāʾ, though not a pronoun, indicates it, and for this reason it takes its place."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سواء كان جمع تكسير نحو: الأيام مضت ومضين، أو جمع سلامة نحو: النخيلات جمع نخيل، وهو القدح الغليظ من الخشب.",
     "en": "Whether a broken plural, as in “al-ayyāmu maḍat” and “maḍayna” (the days passed), or a sound plural, as in “al-nukhaylāt”, plural of “nukhayl”, which is a thick cup of wood."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الصواب: الغير العاقل كما في قوله: وأما في جمع المذكر الغير العاقل؛",
     "en": "The correct reading is “non-rational”, as in his words “as for the plural of a non-rational masculine”;"},
    {"type": "pair",
     "ar": "لأنه يصدق على الرجال أنه جمع المذكر غير السالم مع أنه لا يجوز فيه فعلن.",
     "en": "because “al-rijāl” is truly a masculine plural that is not sound, and yet “faʿalna” is not allowed with it."},
]
