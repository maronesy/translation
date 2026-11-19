# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 545 (printed ٥٤٤)."""

PAGE_NUMBER = 545
PRINTED_PAGE = "٥٤٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(سماعا) سواء» at the foot of PDF p. 544 (mid-sentence).
    {"type": "matn",
     "ar": "لم يكن خبرا، (نحو: «بحسبك زيد»، ﴿وكفى بالله شهيدا[[١]]﴾[[٢]].",
     "en": "…it is not a predicate, (as in “bi-ḥasbika Zaydun” (Zayd suffices you), “And Allah suffices as witness”,"},
    {"type": "matn",
     "ar": "و«ألقى بيده»[[٣]]) أي: حسبك زيد، وكفى بالله شهيدا، وألقى يده.",
     "en": "and “alqā bi-yadihi” (he threw his hand)), that is, “ḥasbuka Zaydun”, “and Allah suffices as witness”, and “alqā yadahu”;"},
    {"type": "matn",
     "ar": "أو كان خبرا، ولكن لا في الاستفهام والنفي، نحو: «حسبك بزيد».",
     "en": "or it is a predicate, but not in interrogation and negation, as in “ḥasbuka bi-Zaydin” (Zayd suffices you)."},

    {"type": "section", "ar": "[اللام]",
     "en": "Al-Lām"},

    {"type": "matn",
     "ar": "(واللام[[٤]]):",
     "en": "(And the lām [is]):"},
    {"type": "matn",
     "ar": "١-(للاختصاص[[٥]]) بملكية[[٦]]، نحو: «المال لزيد»، وبلا ملكية نحو: «الجل للفرس».",
     "en": "1. (for specification (ikhtiṣāṣ)), with ownership, as in “the wealth belongs to Zayd”, and without ownership, as in “the saddle-cloth is for the horse”."},
    {"type": "matn",
     "ar": "٢-(والتعليل) أي: لبيان علة الشيء ذهنا، نحو: «ضربت للتأديب» أو خارجا، نحو: «خرجت لمخافتك».",
     "en": "2. (And for causation (taʿlīl)), that is, for stating the cause of a thing, mentally, as in “I struck for the sake of discipline”, or externally, as in “I went out for fear of you”."},
    {"type": "matn",
     "ar": "٣-(وبمعنى «عن» مع القول) نحو: «قلت لزيد: إنه لم يفعل الشر»، أي: قلت عنه.",
     "en": "3. (And in the sense of “ʿan” (about) with [verbs of] saying), as in “I said of (li-) Zayd: he did not do evil”, that is, I said about him."},
    {"type": "matn",
     "ar": "٤-(وزائدة) نحو: ﴿ردف لكم﴾[[٧]]، أي: ردفكم.",
     "en": "4. (And redundant), as in “[it may be that some of what you seek to hasten] is close behind you (radifa lakum)”, that is, radifakum."},
    {"type": "matn",
     "ar": "٥-(وبمعنى الواو في القسم[[٨]] للتعجب) نحو: «لله لا يؤخر الأجل».",
     "en": "5. (And in the sense of the wāw in oaths, for wonder (taʿajjub)), as in “by Allah (li-llāhi), the appointed term is not delayed”."},
    {"type": "matn",
     "ar": "وإنما يستعمل[[٩]] في الأمور العظام، فلا يقال: «لله لقد طار الذباب».",
     "en": "It is used only in weighty matters; so one does not say “by Allah (li-llāhi), the fly has flown”."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال الزجاج: دخلت الباء في فاعل «كفى» لتضمن معنى «اكتفى».",
     "en": "Al-Zajjāj said: the bāʾ entered upon the agent of “kafā” because [the verb] includes the sense of “iktafā” (to be content with)."},
    {"type": "pair",
     "ar": "وقيل: فاعله مقدر، والتقدير: كفى الاكتفاء بالله، فحذف المصدر، وبقي مفعوله دالا عليه، وعلى هذا لا تكون الباء زائدة.",
     "en": "It has also been said that its agent is implied, the implied form being “kafā al-iktifāʾu bi-llāhi” (being content with Allah suffices); the verbal noun was then elided and its object remained, indicating it. On this view the bāʾ is not redundant."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة النساء: ٧٩.",
     "en": "Qurʾān, Sūrat al-Nisāʾ 4:79."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: نفسه، ولو كان المراد به ألقى نفسه بسبب يده لم تكن الباء زائدة.",
     "en": "That is, himself. If what were meant by it were “he threw himself by means of his hand”, the bāʾ would not be redundant."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "هذه اللام مكسورة مع كل ظاهر إلا مع المستغاث المباشر لـ«يا»، ومفتوحة مع كل مضمر إلا مع ياء المتكلم.",
     "en": "This lām takes kasra with every explicit noun except with the one whose help is sought (al-mustaghāth) directly following “yā”, and takes fatḥa with every pronoun except with the yāʾ of the first person."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ظاهره أنه للإثبات لشيء، والنفي عن غيره. وجرى عليه الفحول،",
     "en": "Its apparent sense is that it is for affirming [a thing] of something and negating it of anything else; the masters have proceeded on this."},
    {"type": "pair",
     "ar": "وذكر بعض المتأخرين: إن معنى الاختصاص مجرد المناسبة لا الحصر؛ إذ لا يصح في «زيد أخ لعمر» وإذا كان أخا بكر أيضا.",
     "en": "Some of the later scholars stated that the meaning of specification is mere association, not restriction (ḥaṣr), since [restriction] would not hold in “Zayd is a brother to ʿAmr” when he is also Bakr’s brother."},
    # REVIEW: «لا ينبغي» is clearly printed; the argument seems to require «لا ينتفي» ("relative specification is not absent"). Transcribed as printed.
    {"type": "pair",
     "ar": "وفيه أنه لا ينبغي الاختصاص الإضافي في موارد استعمالها، فلا داعي إلى صرف الاختصاص عن الظاهر.",
     "en": "Against this: relative specification (al-ikhtiṣāṣ al-iḍāfī) “lā yanbaghī” [as printed; the sense seems to be “is not absent”] in the places where it is used, so there is no reason to divert specification from its apparent sense."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إشارة إلى أن ما ذكروه من معاني اللام من الملك والاستحقاق كلها داخلة في الاختصاص.",
     "en": "An indication that the meanings of the lām they mention, such as ownership and entitlement (istiḥqāq), all fall under specification."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سورة النمل: ٧٢.",
     "en": "Qurʾān, Sūrat al-Naml 27:72."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لم يقل: بمعنى الباء في القسم مع أن الباء أصل تنبيها على أنه كواو القسم لا كبائه.",
     "en": "He did not say “in the sense of the bāʾ in oaths”, although the bāʾ is the original [particle of oaths], to point out that it is like the wāw of oaths, not like its bāʾ."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "إما إشارة إلى أن المراد بالتعجب ما من شأنه أن يتعجب منه على ما في الرضي، أو إلى فائدة زائدة لا بد من اعتبارها إن أريد به المعنى الظاهر.",
     "en": "This is either an indication that what is meant by wonder is whatever is apt to be wondered at, as in al-Raḍī, or [an indication] of an additional point that must be taken into account if its apparent meaning is intended."},
]
