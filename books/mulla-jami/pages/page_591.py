# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 591 (printed ٥٩٠)."""

PAGE_NUMBER = 591
PRINTED_PAGE = "٥٩٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… «يذكر زيد فهو منطلق» بصيغة الفعل» at the foot of PDF p. 590 (mid-sentence).
    {"type": "matn",
     "ar": "الغائب المجهول على أن يكون «زيد» مرفوعا بأنه فاعل الفعل المحذوف،",
     "en": "…of the third person passive, with “Zayd” in the nominative as the agent of the elided verb;"},
    {"type": "matn",
     "ar": "وتقديره على تقدير النصب ب«مهما»: «تذكر يوم الجمعة» بصيغة الفعل المخاطب المعلوم على أن يكون «يوم الجمعة» منصوبا بأنه مفعول به للفعل المحذوف،",
     "en": "and its construction, on the supposition of the accusative, with “mahmā”: “[mahmā] tadhkur yawma l-jumuʿati” (whenever you mention Friday), in the form of the second person active verb, with “yawma l-jumuʿati” in the accusative as the direct object (mafʿūl bihi) of the elided verb —"},
    {"type": "matn",
     "ar": "فوجهه غير ظاهر، مع أنه يوهم جواز «أما زيدا فمنطلق»، بالنصب بتقدير: تذكر على صيغة المعلوم المخاطب،",
     "en": "the rationale for this is not evident; moreover, it suggests the permissibility of “ammā Zaydan fa-munṭaliqun”, in the accusative, on the supposition of “tadhkur” in the second person active form,"},
    {"type": "matn",
     "ar": "وجواز: «أما يوم الجمعة فزيد منطلق» برفع اليوم بتقدير «يذكر» على صيغة المجهول الغائب، مع عدم جوازهما بلا خلاف،",
     "en": "and the permissibility of “ammā yawmu l-jumuʿati fa-Zaydun munṭaliqun”, with “yawm” in the nominative, on the supposition of “yudhkaru” in the third person passive form, although both are impermissible without dispute."},
    {"type": "matn",
     "ar": "وإنما مثل المصنف بما يكون الواسطة بين أما وفائها منصوبة؛ لظهور أمثلة كونها مرفوعة لكثرتها.",
     "en": "The author gave an example in which what stands between ammā and its fāʾ is in the accusative only because examples of its being in the nominative are evident, being so frequent."},

    {"type": "section", "ar": "[حرف الردع]",
     "en": "The Particle of Deterrence"},

    {"type": "matn",
     "ar": "(حرف الردع: «كلا») الردع: «هو الزجر والمنع»،",
     "en": "(The particle of deterrence (ḥarf al-radʿ) is “kallā”). Deterrence is “restraining and preventing”."},
    {"type": "matn",
     "ar": "تقول لشخص: «فلان يبغضك»، فيقول[[١]]: «كلا»، أي: ردعا لك، أي: ليس الأمر كما تقول.",
     "en": "You say to a person, “so-and-so hates you”, and he says “kallā”, that is, as a deterrent to you, meaning: the matter is not as you say."},
    {"type": "matn",
     "ar": "وقد يجيء بعد الطلب لنفي إجابة الطالب، كقولك لمن قال لك: «افعل كذا»: «كلا»، أي: لا يجاب إلى ذلك.",
     "en": "It sometimes comes after a request, to deny compliance with the one requesting, as in your saying to someone who said to you “do such-and-such”: “kallā”, that is, that will not be granted."},
    {"type": "matn",
     "ar": "(وقد جاء) أي: كلا (بمعنى «حقا») والمقصود منه تحقيق مضمون الجملة كقوله تعالى: ﴿كلا إن الإنسان ليطغى﴾[[٢]]،",
     "en": "(And it has come), that is, kallā, (in the sense of “ḥaqqan” (truly)), its purpose being to affirm the content of the sentence, as in His words, the Exalted: “Truly, man transgresses”."},
    {"type": "matn",
     "ar": "وإذا كان بمعنى «حقا» جاز أن يقال: «إنه اسم بني»؛ لكون لفظه كلفظ «كلا» الذي هو حرف، ولمناسبة معناه لمعناه؛",
     "en": "When it is in the sense of “ḥaqqan”, one may say “it is an indeclinable (mabnī) noun”, because its wording is like the wording of the “kallā” that is a particle, and because its meaning is akin to that one’s meaning;"},
    {"type": "matn",
     "ar": "لأنك تردع المخاطب عما يقوله تحقيقا لضده،",
     "en": "for you deter the addressee from what he says in affirmation of its contrary."},
    {"type": "matn",
     "ar": "لكن النحاة حكموا بحرفيته إذا كان بمعنى «حقا» أيضا، لما فهموا من أن المقصود به تحقيق مضمون الجملة، كالمقصود ب«أن» فلم يخرجه ذلك عن الحرفية.",
     "en": "But the grammarians judged it to be a particle when it is in the sense of “ḥaqqan” as well, since they understood that its purpose is to affirm the content of the sentence, like the purpose of “anna”; so that did not remove it from being a particle."},

    {"type": "section", "ar": "[تاء التأنيث الساكنة]",
     "en": "The Quiescent Tāʾ of the Feminine"},

    {"type": "matn",
     "ar": "(تاء التأنيث الساكنة) لا المتحركة؛ لأنها مختصة بالاسم.",
     "en": "(The quiescent tāʾ of the feminine (tāʾ al-taʾnīth al-sākina)), not the vowelled one, since the latter is particular to the noun."},
    {"type": "matn",
     "ar": "(تلحق) الفعل (الماضي) لتكون من أول الأمر علامة (لتأنيث المسند إليه[[٣]]) فاعلا",
     "en": "(It is attached to) the (perfect) verb, so that it may be, from the outset, a sign (of the feminine gender of the subject of predication (al-musnad ilayhi)), whether an agent…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا رد للمخبر، ونفي لخبره،",
     "en": "This is a rejection of the one who informs, and a denial of his report."},
    {"type": "pair",
     "ar": "وقد يكون بيانا لكون خبر أتى به المتكلم منكرا كقوله تعالى: ﴿واتخذوا من دون الله آلهة ليكونوا لهم عزا﴾ (سورة مريم: ٨١).",
     "en": "It may also serve to show that a report the speaker brought is to be rejected, as in His words, the Exalted: “And they have taken gods besides Allah, that they might be for them a source of strength” (Qurʾān, Sūrat Maryam 19:81)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة العلق: ٦.",
     "en": "Qurʾān, Sūrat al-ʿAlaq 96:6."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "تحقيقا أو تنزيلا كما في الجموع المنزلة منزلة المؤنث بالتاء.",
     "en": "Whether really or by assimilation, as with plurals that are treated as feminine with respect to the tāʾ."},
]
