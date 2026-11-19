# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 401 (printed ٤٠٠)."""

PAGE_NUMBER = 401
PRINTED_PAGE = "٤٠٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وكم الخبرية) مميزها (مجرور) بالإضافة (مفرد) تارة (ومجموع) أخرى، تقول:» at the foot of PDF p. 400.
    {"type": "matn",
     "ar": "«كم رجل عندي وكم رجال» كما تقول: «مائة ثوب، وثلاثة أثواب»،",
     "en": "…“kam rajulin ʿindī” (how many a man I have!) “and kam rijālin” (how many men!), just as you say “miʾatu thawbin” (a hundred garments) and “thalāthatu athwābin” (three garments)."},
    {"type": "matn",
     "ar": "وإنما جاء مفردا؛ لأن العدد الكثير مميزه كذلك، وإنما جاء مجموعا؛ لأن العدد الكثير فيه ما ينبئ[[١]] عن كثرته صريحا،",
     "en": "It comes singular only because the specifier of a large number is likewise; and it comes plural only because a large number has in it what expressly announces its largeness;"},
    {"type": "matn",
     "ar": "ولما كان هذا ليس مثله في التصريح بالكثرة، جعل جمعية مميزه، كأنها نائبة عن معنى التصريح بها.",
     "en": "and since this [kam] is not like it in expressly stating largeness, the plurality of its specifier was made as though it stood in for the sense of stating it expressly."},
    {"type": "matn",
     "ar": "(وتدخل «من» فيها) أي: في مميزي «كم» الاستفهامية والخبرية، تقول: «كم من رجل ضربت» و﴿وكم من قرية أهلكناها﴾[[٢]].",
     "en": "(And “min” enters upon them), that is, upon the specifiers of interrogative and predicative “kam”. You say: “kam min rajulin ḍarabta” (how many men did you strike?), and “How many a town have We destroyed!”"},
    {"type": "matn",
     "ar": "قال الشارح الرضي: هذا في الخبرية كثير، نحو: ﴿وكم من ملك﴾[[٣]]، ﴿وكم من قرية﴾[[٤]]، وذلك لموافقته جرا للمميز المضاف إليه «كم»،",
     "en": "The commentator al-Raḍī said: this is frequent with the predicative, as in “How many an angel…” and “How many a town…”; that is because it agrees, in the genitive, with the specifier to which “kam” is annexed."},
    {"type": "matn",
     "ar": "وأما مميز «كم» الاستفهامية، فلم أعثر عليه مجرورا بـ«من» في نظم ولا نثر، ولا دل على جوازه كتاب من كتب هذا الفن.",
     "en": "As for the specifier of interrogative “kam”, I have not come upon it made genitive by “min” in verse or prose, nor does any book of this discipline indicate that it is permitted."},
    {"type": "matn",
     "ar": "لكن جوز الزمخشري[[٥]] أن يكون «كم» في قوله تعالى: ﴿سل بني إسرائيل كم آتيناهم من آية بينة﴾[[٦]] استفهامية وخبرية.",
     "en": "But al-Zamakhsharī allowed “kam” in His words, the Exalted, “Ask the Children of Israel how many a clear sign We gave them” to be either interrogative or predicative."},
    {"type": "matn",
     "ar": "(ولهما) أي: ولـ«كم» استفهامية كانت أو خبرية (صدر الكلام)؛",
     "en": "(And to both), that is, to “kam”, whether interrogative or predicative, (belongs the head of the sentence (ṣadr al-kalām)),"},
    {"type": "matn",
     "ar": "لأن الاستفهامية يتضمن الاستفهام، وهو يقتضي صدر الكلام ليعلم من أول الأمر أنه من أي نوع من أنواع الكلام،",
     "en": "because the interrogative contains interrogation, and that requires the head of the sentence, so that it be known from the outset to which kind of speech it belongs;"},
    {"type": "matn",
     "ar": "والخبرية أيضا تدل على إنشاء التكثير[[٧]]، وهو أيضا نوع من الكلام، فيجب التنبيه عليه من أول الأمر.",
     "en": "and the predicative too indicates the performative expression of multitude (inshāʾ al-taktīr), and that too is a kind of speech, so it must be signalled from the outset."},
    {"type": "matn",
     "ar": "(وكلاهما) لو قال: «كلتاهما» لكان أوفق؛ لتأنيث الاستفهامية والخبرية، فهو على",
     "en": "(And both of them (kilāhumā)): had he said “kiltāhumā” it would have been more consistent, because “interrogative” and “predicative” are feminine; so it is on…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الصواب إسقاط «ما».",
     "en": "The correct reading omits “mā”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة الأعراف: ٤.",
     "en": "Qurʾān, Sūrat al-Aʿrāf 7:4."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة النجم: ٢٦.",
     "en": "Qurʾān, Sūrat al-Najm 53:26."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة الأعراف: ٤.",
     "en": "Qurʾān, Sūrat al-Aʿrāf 7:4."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "رد لما قاله الشيخ الرضي. وجوابه: أن كلامه في مميز متصل بـ«كم».",
     "en": "A rejoinder to what Shaykh al-Raḍī said. Its answer is that his statement concerns a specifier contiguous with “kam”."},
    {"type": "pair",
     "ar": "وأما إذا فصل بينهما بفعل متعد، فالإتيان بـ«من» واجب في الخبرية والاستفهامية ذكره الرضي قبيل هذا الكلام، والآية من قبيل الفصل.",
     "en": "When, however, a transitive verb separates them, bringing in “min” is obligatory with both the predicative and the interrogative; al-Raḍī mentioned this shortly before this statement, and the verse is a case of separation."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "سورة البقرة: ٢١١.",
     "en": "Qurʾān, Sūrat al-Baqara 2:211."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "هذا أولى مما ذكره الفاضل الهندي أن الخبرية نقيضة «رب» التي لإنشاء التقليل؛ لأنه تطويل المسافة بلا فائدة،",
     "en": "This is better than what al-Fāḍil al-Hindī mentioned, that the predicative is the counterpart of “rubba”, which is for the performative expression of fewness, because that lengthens the way without benefit."},
    # REVIEW: «الإنساء» printed (dotless sīn); the context requires «الإنشاء». Transcribed as printed.
    {"type": "pair",
     "ar": "وينبغي أن يعلم أن كون «كم» لإنشاء التكثير، وكون «رب» لإنشاء التقليل لا يخرجان كلاما فيه أحدهما عن الخبرية؛ لأن الإنساء راجع إلى استكثار المتكلم واستقلاله متعلق الحكم الخبري.",
     "en": "It should be known that “kam” being for the performative expression of multitude, and “rubba” being for that of fewness, do not take a sentence containing either of them out of being a statement (khabar), because the performative element goes back to the speaker’s deeming many, or deeming few, the object of the predicative judgement."},
]
