# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 36 (printed ٣٥)."""

PAGE_NUMBER = 36
PRINTED_PAGE = "٣٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "قيد يخرجها[[١]].",
     "en": "a restriction (qayd) that would exclude them."},
    {"type": "matn",
     "ar": "وإنما قال: «لفظ» ولم يقل: «لفظة»؛ لأنه[[٢]] لم يقصد الوحدة[[٣]]، والمطابقة غير لازمة[[٤]]، لعدم الاشتقاق[[٥]] مع كون اللفظ أخصر[[٦]].",
     "en": "He said “lafẓ” (utterance) and did not say “lafẓa” (a single utterance), only because he did not intend oneness (waḥda); and agreement (muṭābaqa) [of predicate with subject] is not obligatory here, owing to the absence of derivation (ishtiqāq), together with “lafẓ” being more concise (akhṣar)."},
    {"type": "matn",
     "ar": "(وضع)[[٧]] الوضع: تخصيص شيء[[٨]] بشيء[[٩]]، بحيث[[١٠]] متى أطلق أو أحس[[١١]] الشيء الأول، فهم[[١٢]] منه الشيء الثاني.",
     "en": "“[That which] is coined (wuḍiʿa)”: coining (al-waḍʿ) is the assignment of one thing to another (takhṣīṣ shayʾ bi-shayʾ), such that whenever the first thing is uttered or perceived, the second thing is understood from it."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: الدوال الأربع.",
     "en": "That is: the four indicators (al-dawāll al-arbaʿ)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: المصنف.",
     "en": "That is: the author."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إما لأن مثل «عبد الله» علما داخل في الكلمة عنده، خارج عنها عند من قال: «لفظة». وأما في قوله: فإنه لا يقال له: لفظة واحدة. وهو الذي ذكره المصنف رحمه الله في الإيضاح.",
     "en": "Either because the like of “ʿAbd Allāh” as a proper name is, in his [view], included within [the term] “kalima” (word), [but] excluded from it in the view of one who says “lafẓa.” And as for [the point] in his statement: [it is] that it is not called of it “a single utterance (lafẓa wāḥida).” This is what the author — may Allah have mercy on him — mentioned in al-Īḍāḥ."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بل غير جائز؛ لأن المصدر لا يحتمل التأنيث والتثنية والجمع، وإن أريد به معنى الصفة، صرح به في الكشاف في تفسير قوله تعالى: ﴿حتى تكون حرضا أو تكون من الهالكين﴾ (سورة يوسف: ٨٥).",
     "en": "Rather it is not even permissible, because the verbal noun (maṣdar) does not admit feminization (taʾnīth), dualization, or pluralization, even if the meaning of the adjective is intended by it. This was stated explicitly in al-Kashshāf, in the exegesis of His words, the Exalted: “until you become emaciated or become of those who perish” (Qurʾān, Sūrat Yūsuf 12:85)."},
    {"type": "pair",
     "ar": "وإنما قيل: غير لازمة اكتفاء بأدنى ما يكفي.",
     "en": "And it was said “not obligatory” only by way of contenting oneself with the least that suffices."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "مطابقة الخبر للمبتدأ مشروطة بثلاثة شروط: الأول: الاشتقاق وما في حكمه. والثاني: الإسناد إلى الضمير الراجع إلى المبتدأ. والثالث: عدم تساوي التذكير والتأنيث ك«جريح». وقد انتفت هنا الثلاثة بأسرها.",
     "en": "The agreement of the predicate with the subject (mubtadaʾ) is conditioned upon three conditions: The first: derivation (ishtiqāq) and what is in its ruling. The second: predication involving a pronoun referring back to the subject. The third: the non-equivalence of the masculine and feminine, as in “jarīḥ” (wounded). Here all three of them are absent."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فيكون الاختصار بترك التاء فقط. والأول هو المتبادر، ولذا قصر عليه العصام.",
     "en": "So the conciseness [consists] in dropping the tāʾ only. This is the [reading] that first comes to mind, and for that reason al-ʿIṣām restricted [it] to it."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "وهو بمنزلة الفصل يخرج الألفاظ المهملة. واعلم أن الفعل الواقع في التعريفات ماضيا كان أو غيره يراد به الاستمرار غالبا.",
     "en": "It [i.e., “wuḍiʿa”] is in the position of the differentia (faṣl): it excludes the neglected utterances (al-alfāẓ al-muhmala). And know that the verb occurring in definitions — whether past-tense or otherwise — is generally intended to convey continuity (istimrār)."},
    {"type": "pair",
     "ar": "قوله: «الوضع» في اللغة: جعل الشيء في حيز، فكأن الواضع بتعيينه يجعل المعنى حيز اللفظ.",
     "en": "His statement “al-waḍʿ” (coining): in the [lexical] language it is the placing of a thing in a receptacle (ḥayyiz); it is as though the coiner (wāḍiʿ), by his designating [it], makes the meaning [occupy] the receptacle of the utterance."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "ملحوظ بخصوصه أو بعمومه، كهيئة المفردات والمركبات.",
     "en": "[A thing] regarded either in its particularity or in its generality, like the form (hayʾa) of simple words and of compounds."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "سواء كان ملحوظا بخصوصه أو بعمومه، ولا يدخل في الموضوع المحرف؛ لأن الحرف الأول لم يقصد جعله في حيز، بل قصد المعنى به، يتوهم أنه مجعول له.",
     "en": "Whether [the second thing be] regarded in its particularity or in its generality. The mutated [form] (al-muḥarraf) does not enter into “the coined” (al-mawḍūʿ), because the first letter (al-ḥarf al-awwal) — its being placed in a receptacle is not intended; rather the meaning is intended by it, [though] it is [only] imagined that it is made [placed] for it."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: حال كون ذلك الشيء المخصص ملابسا لتلك الحيثية التي هي مضمون الشرطية. وبه يخرج تخصيص حروف الهجاء لغرض التركيب.",
     "en": "That is: while that specified thing is clothed in (mulābisan) that aspect (ḥaythiyya) which is the content of the conditional. By this, the specifying of the letters of the alphabet for the purpose of composition (tarkīb) is excluded."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "بغير السمع. وهو تنبيه على قسمي الموضوع من اللفظ وغيره كالدوال الأربع، وإلا فيكفي أن يقال: «متى أحس».",
     "en": "By [a sense] other than hearing. This is an alerting to the two kinds of “the coined” — the utterance and other than it, like the four indicators; otherwise it would suffice to say “whenever it is perceived.”"},
    {"type": "pair",
     "ar": "إن قلت: إن الكلية غير صادقة إلا بعد انضمام العلم بالتخصيص إلى الشرط؟",
     "en": "If you say: the universal [proposition] is not true except after the joining of knowledge of the specification to the condition[al]?"},
    {"type": "pair",
     "ar": "قلنا: لا يبعد أن يقال: هذا الانضمام مراد ومفهوم من العبارة؛ فإن العبارة ظاهرة في أن التخصيص علاقة بها يثبت الدلالة، ومن المعلوم أنه لا بد في الدلالة من العلم بالعلاقة، فكأنه قال: متى أطلق أو أحس وعلم ذلك التخصيص.",
     "en": "We say: it is not far-fetched to say that this joining is intended and understood from the expression; for the expression is apparent in [conveying] that the specification is a relation (ʿalāqa) by which the signification (dalāla) is established, and it is known that signification necessarily requires knowledge of the relation — so it is as though he said: “whenever the first thing is uttered or perceived and that specification is known.”"},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "إن لم يكن مفهوما، أو فهم منه قصد والتفات، فلا يرد شبهة تحصيل الحاصل.",
     "en": "If it [the second thing] be not [already] understood, or [if] intent and attention toward it be understood from it, then the objection of “obtaining the [already-]obtained” (taḥṣīl al-ḥāṣil) does not arise."},
]
