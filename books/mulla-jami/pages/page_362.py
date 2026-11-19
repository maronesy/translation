# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 362 (printed ٣٦١)."""

PAGE_NUMBER = 362
PRINTED_PAGE = "٣٦١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(فالمرفوع المتصل خاصة) يعني: لا المنصوب والمجرور المتصلان (يستتر)؛» from the foot of PDF p. 361.
    {"type": "matn",
     "ar": "لأنهما فضلة، والمرفوع فاعل، وهو كجزء الفعل،",
     "en": "…because those two are supplements (faḍla), whereas the nominative is the agent, and it is like a part of the verb."},
    {"type": "matn",
     "ar": "فجوزوا في باب الضمائر التي وضعها للاختصار[[١]] استتار الفاعل[[٢]]، فاكتفوا بلفظ الفعل",
     "en": "So in the chapter of pronouns, whose coinage is for brevity, they permitted the agent to be concealed and made do with the wording of the verb,"},
    {"type": "matn",
     "ar": "كما يحذف في آخر الكلمة المشتهرة[[٣]] شيء، ويكون فيما بقي دليل على ما ألقي على ما مضى في الترخيم،",
     "en": "just as something is elided at the end of a well-known word, with what remains indicating what was dropped, as has passed in [the chapter of] truncation (tarkhīm)."},
    {"type": "matn",
     "ar": "ولكن هذا الاستتار ليس في جميع الصيغ، بل (في) الفعل (الماضي للغائب) الواحد المذكر إذا لم يكن مسندا إلى الظاهر نحو: «زيد ضرب»",
     "en": "But this concealment is not in all forms; rather, it is (in) the (past) verb (for the absent) masculine singular, when it is not attributed to an overt noun, as in “Zaydun ḍaraba” (Zayd struck),"},
    {"type": "matn",
     "ar": "(و) للواحدة المؤنثة (الغائبة) إذا لم يكن مسندة إلى الظاهر نحو: «هند ضربت»،",
     "en": "(and) for the (absent) feminine singular, when it is not attributed to an overt noun, as in “Hindun ḍarabat” (Hind struck);"},
    {"type": "matn",
     "ar": "فإن التاء علامة التأنيث لا الضمير المرفوع، وإلا لم يجتمع مع الفاعل الظاهر نحو: «ضربت هند»،",
     "en": "for the tāʾ is the mark of the feminine, not the nominative pronoun; otherwise it would not combine with an overt agent, as in “ḍarabat Hindun”."},
    {"type": "matn",
     "ar": "وفي الفعل (المضارع للمتكلم[[٤]] مطلقا[[٥]]) سواء كان مثنى أو مجموعا أو واحدا أو فوق الواحد[[٦]]، مذكرا أو مؤنثا نحو: «أضرب ونضرب»",
     "en": "And in the (imperfect) verb (for the first person, without qualification), whether dual or plural, or singular or more than one, masculine or feminine, as in “aḍribu” (I strike) and “naḍribu” (we strike);"},
    {"type": "matn",
     "ar": "(و) للواحد (المخاطب) المذكر نحو: «تضرب واضرب»",
     "en": "(and) for the masculine singular (addressee), as in “taḍribu” (you strike) and “iḍrib” (strike!);"},
    {"type": "matn",
     "ar": "(و) للواحد (الغائب والغائبة) إذا لم يكونا مسندين إلى الظاهر نحو: «زيد",
     "en": "(and) for the singular (absent, masculine and feminine), when they are not attributed to an overt noun, as in “Zaydun…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: المنظور في هذا الباب الاختصار.",
     "en": "That is: what is aimed at in this chapter is brevity."},
    {"type": "pair",
     "ar": "أما أولا: فبأخذ المعاني المقتضية للإعراب في مدلولاتها لئلا يحتاجوا إلى الإعراب.",
     "en": "First, by taking the meanings that call for inflection into what they signify, so that they do not need inflection."},
    {"type": "pair",
     "ar": "وأما ثانيا: فبقلة الحروف، وهي في المتصلة ظاهرة.",
     "en": "Second, by the fewness of letters, which is evident in the attached [pronouns]."},
    {"type": "pair",
     "ar": "وأما في المنفصلة: فلأنك إذا عبرت عن نفسك وعن غيرك بأسمائهما وجدت غالبا أن الضمير أقل حروفا منهما.",
     "en": "As for the detached ones: when you refer to yourself and to another by their names, you will usually find the pronoun to have fewer letters than they."},
    {"type": "pair",
     "ar": "وأما ثالثا: فبعدم الاحتياج إلى قرينة ترفع الالتباس الذي في الأسماء الظاهرة،",
     "en": "Third, by not needing a contextual indication (qarīna) to remove the ambiguity found in overt nouns:"},
    {"type": "pair",
     "ar": "فإنك إذا قلت: زيد مثلا التبس على المخاطب أنه زيد العالم أو الجاهل، فيحتاج في تعيين المراد إلى قرينة.",
     "en": "if you say “Zayd”, for example, the addressee is unsure whether it is Zayd the learned or the ignorant, and so a contextual indication is needed to fix what is meant."},
    {"type": "pair",
     "ar": "وإذا قلت: «أنت، أو أنا، أو هو» بعد سبق المرجع لم يحتج إلى قرينة تزيل الالتباس.",
     "en": "But if you say “anta”, “anā” or “huwa” after the referent has preceded, no indication is needed to remove ambiguity."},
    {"type": "pair",
     "ar": "وإذا عرفت ذلك فالأصل في هذا الباب المتصل المستتر؛ لأنه أخصر، ثم المتصل البارز، ثم المنفصل.",
     "en": "Once you know this, the default in this chapter is the concealed attached pronoun, because it is the briefest, then the visible attached pronoun, then the detached."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ليس المستتر من مقولة الصوت والحرف، ولا أدري من أي مقولة هو.",
     "en": "The concealed [pronoun] does not belong to the category of sound and letter, and I do not know to which category it belongs."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ظاهره يدل على أن الفاعل المستتر هو المحذوف، وهو الذي ذهب إليه المصنف.",
     "en": "Its apparent sense indicates that the concealed agent is the elided one, which is the position the author took."},
    # REVIEW: «وقال الآن» as printed; the subject of «قال» is not named.
    {"type": "pair",
     "ar": "وقال الآن: إن النحاة لا يطلقون المحذوف على المستتر كراهة لحذف الفاعل، وهذا كلام ظاهري،",
     "en": "He said now: the grammarians do not call the concealed [pronoun] “elided” out of aversion to eliding the agent. This is a superficial statement;"},
    {"type": "pair",
     "ar": "والتحقيق ما سبق في أوائل الشرح وبلغنا فيه بلطف الله تعالى نهاية التحقيق، فلا تغفل عنه إن كنت من أهل التدقيق.",
     "en": "the precise view is what preceded at the beginning of the commentary, where, by the grace of Allah the Exalted, we reached the utmost precision; so do not neglect it if you are one of the people of close scrutiny."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "صفة للمضارع.",
     "en": "An adjective qualifying “al-muḍāriʿ”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: زمانا مطلقا أو استتارا مطلقا، والظاهر ما قاله الشارح من أنه بيان للمتكلم، وكذا الحال في قوله: وفي الصفة مطلقا.",
     "en": "That is: “at any time” or “with unqualified concealment”; but the apparent [reading] is what the commentator said, that it specifies “the first person”. The same holds of his words “and in the adjective without qualification”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "كأنه سهو من قلم الناسخ.",
     "en": "It seems to be a slip of the copyist’s pen."},
    {"type": "pair",
     "ar": "وفي الهندي: واحد أو مثنى أو مجموعا مذكرا أو مؤنثا، وكان الشارح غيره إلى الواحد أو فوق الواحد؛ لأنه أخصر وأوضح؛",
     "en": "In al-Hindī: “singular, or dual, or plural, masculine or feminine”; and the commentator changed it to “singular or more than one”, because it is briefer and clearer,"},
    {"type": "pair",
     "ar": "لأنه لا يطلق في العرف المثنى على اثنين، بل على اللفظ المخصوص والمجموع على ما فوق الاثنين، بل على اللفظ المخصوص،",
     "en": "since in conventional usage “dual” is not applied to two [persons] but to the specific word-form, and “plural” not to more than two but to the specific word-form."},
    {"type": "pair",
     "ar": "فالصحيح أنه ليس في الشرح مثنى أو مجموعا، والأوفق بالمشهور تفسير مطلقا بوحده أو مع الغير،",
     "en": "So the correct view is that “dual or plural” is not in the commentary, and what better accords with the well-known [usage] is to explain “without qualification” as “alone or with another”."},
    {"type": "pair",
     "ar": "وهذا يرشد إلى أن مطلقا حال من المتكلم لا ظرف زمان أي: زمانا مطلقا ولا منصوبا لقوله: يستتر مصدرا كان أو حالا أو ظرفا.",
     "en": "This shows that “muṭlaqan” is a circumstantial qualifier of “the first person”, not an adverb of time, that is, “at any time”, nor in the accusative by his word “yastatiru”, whether as a verbal noun, a circumstantial qualifier or an adverb."},
]
